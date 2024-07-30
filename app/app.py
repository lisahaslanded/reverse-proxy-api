from flask import Flask
import random

app = Flask(__name__)

dice = [n for n in range(1, 7)]

@app.route("/dice", methods=["GET"])
def roll_dice(num_dice=2):
  '''roll two dice and return result'''
  result = {}
  for i in range(num_dice):
    result["dice " + str(i)] = random.choice(dice)
  return result

if __name__ == "__main__":
    app.run(debug=True, host="192.168.56.4", port="8080")