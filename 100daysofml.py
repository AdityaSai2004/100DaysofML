{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "100daysofml.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMfQjqNkW8+LygZPV3oIzbG",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AdityaSai2004/100DaysofML/blob/main/100daysofml.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Day 3**"
      ],
      "metadata": {
        "id": "5lszZLFGnkLm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import tensorflow as tf\n",
        "from tensorflow import keras"
      ],
      "metadata": {
        "id": "eJ4XUwtGnxk2"
      },
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X=[0,1,2,3,4,5,6]\n",
        "Y=[0.5,0.6,0.7,0.8,0.9,1.0,1.1]\n",
        "def salary_model(y_new):\n",
        "  model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])\n",
        "  model.compile(optimizer=\"sgd\", loss='mean_squared_error')\n",
        "  model.fit(X, Y, epochs=500)\n",
        "  return model.predict(y_new)[0][0]"
      ],
      "metadata": {
        "id": "pGn5DSFUpSRe"
      },
      "execution_count": 38,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "prediction = salary_model([8.0])"
      ],
      "metadata": {
        "id": "P72pLYDQ8qh5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(prediction)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "h_Y7DVnt8390",
        "outputId": "44255fb5-c0e0-4d92-b051-e07348f82139"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1.3211551\n"
          ]
        }
      ]
    }
  ]
}