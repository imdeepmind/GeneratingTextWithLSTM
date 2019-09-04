# Data related constants
DATABASE="dataset"
NO_ROWS_VAL=1000000 #19981962
NO_ROWS_TRAIN=1000000 #159855696
NO_ROWS_TEST=19981962
ONE_HOT_MODE=False

# Model related constants
GPU=True
BATCH_SIZE=4096
MAX_LENGTH=40
EPOCHS=1000

# Prediction and demo related connstants
DEMO_REVIEW="so if you're looking for earphones playi"
PREDICT_CHARS=500
TEMPERATURE=[0.2, 0.5, 1.0, 1.2]

# Other
WEIGHT_FOLDER='weights'