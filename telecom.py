{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "telecom.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "mount_file_id": "1IcGP59QuRyZzV4QvNL0J1kks7FgcrsS6",
      "authorship_tag": "ABX9TyMxuIL4wz0KqDjdS/C2jAO0",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/duhajarrar/TelecomMIT/blob/main/telecom.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8zUejHvJdXE_"
      },
      "source": [
        "import pandas as pd\r\n",
        "import numpy as np\r\n",
        "trainingData = pd.read_csv(\"drive/My Drive/python/telecom.csv\")\r\n"
      ],
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QXR7pKzxd6VG",
        "outputId": "20029c57-10e8-4ad3-b39a-377a060e9bb0"
      },
      "source": [
        "trainingData.info()"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 3333 entries, 0 to 3332\n",
            "Data columns (total 21 columns):\n",
            " #   Column                  Non-Null Count  Dtype  \n",
            "---  ------                  --------------  -----  \n",
            " 0   state                   3333 non-null   object \n",
            " 1   account length          3333 non-null   int64  \n",
            " 2   area code               3333 non-null   int64  \n",
            " 3   phone number            3333 non-null   object \n",
            " 4   international plan      3333 non-null   object \n",
            " 5   voice mail plan         3333 non-null   object \n",
            " 6   number vmail messages   3333 non-null   int64  \n",
            " 7   total day minutes       3333 non-null   float64\n",
            " 8   total day calls         3333 non-null   int64  \n",
            " 9   total day charge        3333 non-null   float64\n",
            " 10  total eve minutes       3333 non-null   float64\n",
            " 11  total eve calls         3333 non-null   int64  \n",
            " 12  total eve charge        3333 non-null   float64\n",
            " 13  total night minutes     3333 non-null   float64\n",
            " 14  total night calls       3333 non-null   int64  \n",
            " 15  total night charge      3333 non-null   float64\n",
            " 16  total intl minutes      3333 non-null   float64\n",
            " 17  total intl calls        3333 non-null   int64  \n",
            " 18  total intl charge       3333 non-null   float64\n",
            " 19  customer service calls  3333 non-null   int64  \n",
            " 20  churn                   3333 non-null   bool   \n",
            "dtypes: bool(1), float64(8), int64(8), object(4)\n",
            "memory usage: 524.2+ KB\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}