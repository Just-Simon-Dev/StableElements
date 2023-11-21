import keras


def createModel():
    model = keras.Sequential(
        [
            keras.Input(shape=(2,), name="input"),
            keras.layers.Dense(
                120,
                activation=keras.activations.relu,
            ),
            keras.layers.Dense(
                5,
                activation=keras.activations.elu,
            ),
            keras.layers.Dense(
                1, activation=keras.activations.sigmoid, name="predictions"
            ),
        ]
    )
    # model.summary()
    model.compile(
        optimizer=keras.optimizers.Adam(0.001),  # Optimizer
        loss=keras.losses.binary_crossentropy,
        metrics=[keras.metrics.BinaryAccuracy()],
    )

    return model