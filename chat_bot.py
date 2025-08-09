class chatbot :
    def __init__(self):
        self.key_word = {
                    
                    "hello" : "Hi how may i help today ? 🤔",
                    "i need help" : "Im happy to serve 😊",
                    "happy day" : " I'm glad your here ",
                    "exit" : "thanks for chat with me today 😎"
                }
        
        
    def reason (self):
        while True :
            user_input = input("welcome to my simple chat bot say anything you want : ").lower().strip()

            if user_input in self.key_word :
                print(self.key_word[user_input])

                if user_input  == "exit":
                    print(self.key_word[exit])
                    break
            else:
                print("Sorry i cant understand you in this version 😅.")

robot = chatbot()
robot.reason()
