from __future__ import print_function, division

from keras.datasets import mnist
from keras.layers import Input, Dense, Reshape, Flatten, Dropout
from keras.layers import BatchNormalization, Activation, ZeroPadding2D
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.convolutional import UpSampling2D, Conv2D
from keras.models import Sequential, Model
from keras.optimizers import Adam

import matplotlib.pyplot as plt
plt.switch_backend('agg')

import sys
sys.path.insert(0, "/home/service/analyticsBot-sc2/modules")
from Status.Status import Status
from Normalize.NManager import NManager

import numpy as np

class GAN():
    def __init__(self):
        self.status = Status("GAN")
        self.cols = 7
        self.img_shape = (self.cols,)

        optimizer = Adam(0.0002, 0.5)

        # Build and compile the discriminator
        self.discriminator = self.build_discriminator()
        self.discriminator.compile(loss='binary_crossentropy',
            optimizer=optimizer,
            metrics=['accuracy'])

        # Build and compile the generator
        self.generator = self.build_generator()
        self.generator.compile(loss='binary_crossentropy', optimizer=optimizer)

        # The generator takes noise as input and generated imgs
        z = Input(shape=(7,))
        img = self.generator(z)

        # For the combined model we will only train the generator
        self.discriminator.trainable = False

        # The valid takes generated images as input and determines validity
        valid = self.discriminator(img)

        # The combined model  (stacked generator and discriminator) takes
        # noise as input => generates images => determines validity
        self.combined = Model(z, valid)
        self.combined.compile(loss='binary_crossentropy', optimizer=optimizer)

    def build_generator(self):
        self.status.message(1, "build_generator(self)")

        noise_shape = (7,)

        model = Sequential()

        model.add(Dense(7, input_shape=noise_shape))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(7))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(7))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(np.prod(self.img_shape), activation='tanh'))
        model.add(Reshape(self.img_shape))

        #model.summary()

        noise = Input(shape=noise_shape)
        img = model(noise)

        self.status.message(0, "build_generator(self)")
        return Model(noise, img)

    def build_discriminator(self):
        self.status.message(1, "build_discriminator(self)")

        shape = (self.cols,)

        model = Sequential()

        #model.add(Flatten(input_shape=shape))
        model.add(Dense(7))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(1, activation='sigmoid'))
        # model.summary()

        example = Input(shape=shape)
        validity = model(example)

        self.status.message(0, "build_discriminator(self)")
        return Model(example, validity)

    def train(self, trainset, epochs, batch_size=128, save_interval=50):
        # self.status.message(1, "train(self, trainset, epochs, batch_size, save_interval)")

        # Load the dataset
        #(X_train, _), (_, _) = mnist.load_data()
        X_train = trainset

        # Rescale -1 to 1
        X_train = (X_train.astype(np.float32) - 127.5) / 127.5
        #X_train = np.expand_dims(X_train, axis=3)

        half_batch = int(batch_size / 2)

        for epoch in range(epochs):

            # ---------------------
            #  Train Discriminator
            # ---------------------

            # Select a random half batch of images
            idx = np.random.randint(0, X_train.shape[0], half_batch)
            imgs = X_train[idx]

            noise = np.random.normal(0, 1, (half_batch, 7))

            # Generate a half batch of new images
            gen_imgs = self.generator.predict(noise)

            # Train the discriminator
            d_loss_real = self.discriminator.train_on_batch(imgs, np.ones((half_batch, 1)))
            d_loss_fake = self.discriminator.train_on_batch(gen_imgs, np.zeros((half_batch, 1)))
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)


            # ---------------------
            #  Train Generator
            # ---------------------

            noise = np.random.normal(0, 1, (batch_size, 7))

            # The generator wants the discriminator to label the generated samples
            # as valid (ones)
            valid_y = np.array([1] * batch_size)

            # Train the generator
            g_loss = self.combined.train_on_batch(noise, valid_y)

            # Plot the progress
            if epoch % 10 == 0:
                print ("Epoch: %d [Discriminator loss: %f, acc.: %.2f%%] [Generator loss: %f]" % (epoch, d_loss[0], 100*d_loss[1], g_loss))

            # If at save interval => save generated image samples
            if epoch % save_interval == 0:
                self.save_imgs(epoch)

            # self.status.message(0, "train(self, trainset, epochs, batch_size, save_interval)")
            # return

    def save_imgs(self, epoch):
        self.status.message(1, "save_imgs(self, epoch)")
        rows = 10
        noise = np.random.normal(0, 1, (rows, 7))
        gen_imgs = self.generator.predict(noise)

        # Rescale images 0 - 1
        gen_imgs = 0.5 * gen_imgs + 0.5

        cnt = 0
        for i in gen_imgs:
            normalizer = NManager(i)
            print(normalizer.normalstats)

        self.status.message(0, "save_imgs(self, epoch)")
        return
