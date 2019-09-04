# Data related constants
DATABASE="dataset"
NO_ROWS_VAL=10000 #19981962
NO_ROWS_TRAIN=10000 #159855696
NO_ROWS_TEST=19981962
ONE_HOT_MODE=False
OUTPUT_CLASSES=128
VOCAB_SIZE=128

# Model related constants
GPU=False
BATCH_SIZE=int(1024*.25)
MAX_LENGTH=40
EPOCHS=1000

# Prediction and demo related connstants
DEMO_REVIEW="so if you're looking for earphones playi"
PREDICT_CHARS=500
TEMPERATURE=[0.2, 0.5, 1.0, 1.2]

# Other
WEIGHT_FOLDER='weights'