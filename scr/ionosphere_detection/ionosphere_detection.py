import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import roc_auc_score, average_precision_score
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import roc_curve, precision_recall_curve
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

print(tf.config.list_physical_devices())

#Para tener siempre una misma semilla de aleatoreidad
SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)

#Cargar el dataset
data = pd.read_csv('ionosphere.csv', header=None)
X = data.iloc[:, :-1].values.astype(np.float32)
Y = (data.iloc[:, -1] == 'g').astype(np.int32)

print(f"Forma de X: {X.shape}")
print(f"Forma de Y: {Y.shape}")


#Division de mi dataset
#x=características
#y=etiqueta
X_train, X_temp, Y_train, Y_temp = train_test_split(
  X,Y,
  test_size=0.3,
  stratify=Y,
  random_state=SEED)

X_val, X_test, Y_val, Y_test = train_test_split(
  X_temp,Y_temp,
  test_size=0.5,
  stratify=Y_temp,
  random_state=SEED)

#Scaling
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_val_s = scaler.transform(X_val)
X_test_s = scaler.transform(X_test)

#Balance de las clases
classes = np.array([0, 1])
cw = compute_class_weight(class_weight='balanced', classes=classes, y=Y_train)
class_weight = {0: float(cw[0]), 1:float(cw[1])}

#Modelo de red neuronal
#Una epoca hace referencia a toda una vuelta a el dataset
# el dropout hace referencia a que en el entrenamiento se apagan cierto numero
#de neuronas aleatoriamente esto para que nuestra red neuronal evite aprenderse
#el data set
def build_model(input_dim):
  inputs =tf.keras.Input(shape=(input_dim,))
  x = tf.keras.layers.Dense(32, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.001))(inputs)
  x = tf.keras.layers.Dropout(0.15)(x)
  x = tf.keras.layers.Dense(16, activation='relu',  kernel_regularizer=tf.keras.regularizers.l2(0.001))(x)
  x = tf.keras.layers.Dropout(0.10)(x)
  outputs = tf.keras.layers.Dense(1, activation='sigmoid')(x)
  return tf.keras.Model(inputs, outputs)

model = build_model(X_train_s.shape[1])

#Metricas
metrics= [
    tf.keras.metrics.AUC(curve='ROC', name='auc_roc'),
    tf.keras.metrics.AUC(curve='PR', name='auc_pr'),
    tf.keras.metrics.Recall(name='Recall'),
    tf.keras.metrics.Precision(name='Precision')
]

#Compilacion y entrenamiento de mi modelo
model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-3),
    loss='binary_crossentropy',
    metrics=metrics
)

# CallBacks - EarlyStopping
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_auc_roc',
        mode='max',
        patience=40,
        restore_best_weights=True)
]

lr=0.001
model.compile(
    optimizer=tf.keras.optimizers.Adam(lr),
    loss='binary_crossentropy',
    metrics=metrics
)
history = model.fit(
    X_train_s, Y_train,
    validation_data = (X_val_s, Y_val),
    epochs=200,
    batch_size=16,
    class_weight=class_weight,
    verbose=1,
    callbacks=callbacks
    )

# Graficacion
plt.figure()
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('PERDIDA')
plt.legend(['train', 'validation'])
plt.show()

pred_test = model.predict(X_test_s).ravel()

auc_roc = roc_auc_score(Y_test, pred_test)
auc_pr = average_precision_score(Y_test, pred_test)

print("AUC-ROC:", auc_roc)
print("AUC-PR:", auc_pr)

thresholds = np.linspace(0.05, 0.95, 50)

def evaluate_threshold(t):
    y_pred = (pred_test >= t).astype(int)
    cm = confusion_matrix(Y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()
    recall = tp / (tp + fn + 1e-12)
    precision = tp / (tp + fp + 1e-12)
    return cm, precision, recall

target_recall = 0.98
best_threshold = 0.40
best_precision = -1

recall_values = []
precision_values = []

for t in thresholds:
    cm, precision, recall = evaluate_threshold(t)
    recall_values.append(recall)
    precision_values.append(precision)

    if recall >= target_recall and precision > best_precision:
        best_precision = precision
        best_threshold = t

cm, precision, recall = evaluate_threshold(best_threshold)
tn, fp, fn, tp = cm.ravel()

print("Threshold:", best_threshold)
print("Confusion Matrix:\n", cm)
print("Recall:", recall)
print("Precision:", precision)
print("False Negatives:", fn)

y_pred = (pred_test >= best_threshold).astype(int)

print(classification_report(
    Y_test,
    y_pred,
    target_names=["Malo", "Bueno"]
))

plt.figure()
plt.plot(history.history["loss"])
plt.plot(history.history["val_loss"])
plt.title("Loss")
plt.legend(["Train", "Validation"])
plt.show()

plt.figure()
plt.plot(history.history["auc_roc"])
plt.plot(history.history["val_auc_roc"])
plt.title("AUC ROC")
plt.legend(["Train", "Validation"])
plt.show()

plt.figure()
plt.plot(history.history["Recall"])
plt.plot(history.history["val_Recall"])
plt.title("Recall")
plt.legend(["Train", "Validation"])
plt.show()

fpr, tpr, _ = roc_curve(Y_test, pred_test)

plt.figure()
plt.plot(fpr, tpr)
plt.plot([0, 1], [0, 1])
plt.title(f"ROC Curve (AUC={auc_roc:.3f})")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.show()

precision_curve, recall_curve, _ = precision_recall_curve(Y_test, pred_test)

plt.figure()
plt.plot(recall_curve, precision_curve)
plt.title(f"Precision-Recall Curve (AUC={auc_pr:.3f})")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.show()

plt.figure()
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.colorbar()
plt.xticks([0,1], ["Malo", "Bueno"])
plt.yticks([0,1], ["Malo", "Bueno"])
plt.xlabel("Predicted")
plt.ylabel("True")

for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.show()

plt.figure()
plt.plot(thresholds, recall_values)
plt.title("Recall vs Threshold")
plt.xlabel("Threshold")
plt.ylabel("Recall")
plt.show()