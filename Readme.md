# Rock Paper Scissor 

A rock paper scissor game using machine learning.


## Requirements
- Python 3
- DenseNet121
- Keras
- Tensorflow
- OpenCV

## Instructions for setting up
1. Clone the repo.
```sh
$ git clone https://github.com/njnaman/Rock-Paper-Scissors.git
$ cd "Rock Paper Scissor"
```

2. Install the dependencies
```sh
$ pip install -r requirements.txt
```

3. Gather Images for each gesture (rock, paper and scissors and None):
In this example, we gather 50 images for the "Rock" gesture
```sh
$ python3 gather_data.py Rock 50
```

4. Augmenting the data
```sh
$ python3 data_augment.py path
```


5. Train the model
```sh
$ python3 train_densenet.py
```

6. Play the game with your Friends!
```sh
$ python3 play.py
```

# ENJOY THE GAME