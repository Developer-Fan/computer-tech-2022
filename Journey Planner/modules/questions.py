
# In order to make asking questions easier, I have defined a 'question' class.
# This allows us to ask a question whenever we want, and it will return a
# valid answer every time(refer to ask() function) and thus, making it much easier
# for us to ask questions and process inputs which we expect to be inputted.


class question:
    def __init__(self, q, validans):
        self.ques = q
        self.ans = validans

    def ask(self):
        strAns = ""
        if self.ans != "PosInt" and self.ans != "string":  # Special cases excluded
            for i in range(len(self.ans)):
                if i == len(self.ans) - 1:
                    strAns += self.ans[i]
                else:
                    strAns += self.ans[i] + "/"
                    # strAns is a string of all the valid answers, each seperated by a "/"
                    # stripped from validans to make it easier to read
        elif self.ans == "PosInt":  # Special case 1
            strAns = "positive integer"
        elif self.ans == "string":  # Special case 2
            strAns = "text"
        invalid = True  # Used to check if the input is valid
        while invalid:  # Will repeat until the input is valid
            answer = input(f"{self.ques}?({strAns}) ")
            # PosInt is a special case, it only requires the input to be any positive integer
            # string is a special case, it only requires the input to be any string
            if answer in self.ans and self.ans != "PosInt" and self.ans != "string":
                return answer.lower()
            elif answer.isdigit() and self.ans == "PosInt":
                return int(answer)
            elif type(answer) is str and self.ans == "string":
                return str(answer)
            else:
                print("Invalid input. Please try again.")
