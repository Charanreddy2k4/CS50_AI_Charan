from logic import *

rain=Symbol("rain")
hagrid=Symbol("hagrid")
dumbledore=Symbol("dumbledore")

knowledge=And(
    Implication(Not(rain),hagrid),
    Or(hagrid,dumbledore),
    Not(And(hagrid,dumbledore)),
    dumbledore
)
def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge,symbol):
            termcolor.cprint(f"{symbol}:Yes","green")
        elif not model_check(knowledge,Not(symbol)):
            print(f"{symbol}:MAYBE")

knowledge=And(
    Or(mustard,plum,scarley),

)

knowledge.add(Not(mustard))
knowledge.add(Not(mustard))
knowledge.add(Not(mustard))

print(model_check(knowledge,rain))
