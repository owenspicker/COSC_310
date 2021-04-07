# Owen Spicker COSC_310 Individual Project

This is a project to create a functional chatbot for COSC 310. The user should be able to hold basic conversation with the bot about sports. The role the agent will take is that of a friend, and the user can ask the agent questions about sports. This bot was built off of the previous bot created in assignment 3 (team 3). This program uses modified code from https://github.com/nltk/nltk/blob/develop/nltk/chat/util.py which is open source.

New API's that have been implemented in this bot is the Google Translate API, and the Wikipedia API. 
To be able to run this bot with the new features, you will need to install new packages.
# For Wikipedia API, you will need to run "pip install wikipedia".
# For Google Translate API, you will need to run "pip install googletrans==3.1.0a0".
The current edition of the package does not work, so an older package is needed.

The Google Translate API adds to the flow of the conversation by detecting and translating the user input if it is not english. When the user inputs a phrase, it is passed to a method that checks the language. If it is not english, the function will translate the input into english, then return the input back so that it can converse with the chat bot in english. If the phrase is english, the method will return the original phrase back. The translate API supports several languages, however it does struggle with languages that have different characters. It is most effective with languages such as French, Portuguese, German, etc.

Example convo:

Olá (Hello)

                         Hi, what is your name?
                         
je m'appelle Greg (My name is Greg)

                        Hello greg, my name is sports bot. Do you play any sports

Wer ist dein Lieblingsspieler (Who is your favourite player)

                        Loui Erikkson of the Vancouver Canucks, he definitely deserves his $36 million contract
                        
                        
The Wikipedia API adds to the chat bot by allowing the user to ask general definition questions about anything related to sports (or outside of sports too). In order to access the Wikipedia API, the user has to form the question as: "Tell me about _ ". This statement triggers to program to search the Wikipedia API. The input is taken in, and returns the first sentence from Wikipedia (which is usually a general statement about the topic). If the article is not found, the chat bot will inform the user that it cannot find any information on that topic. The Wikipedia API will sometimes struggle, escpecially with athelete names. For example, if you ask about "Connor McDavid", the chatbot can't find any information. However, it will recognize "Connor Andrew McDavid" and return information. Spelling especially matters with this API. It responds effectively with most topics, just not as much with athlete names.

Example convo:

Tell me about Kelowna Rockets

                      The Kelowna Rockets are a major junior ice hockey team based in Kelowna, British Columbia, Canada.

Tell me about Allianz Arena

                      Allianz Arena [ʔali̯ˈants ʔaˌʁeːnaː] (known as Fußball Arena München for UEFA competitions) is a football stadium in Munich, Bavaria, Germany with a 70,000 seating capacity for international matches and 75,000 for domestic matches.

Tell me about Michael Jordan

                      Michael Jeffrey Jordan (born February 17, 1963), also known by his initials MJ, is an American businessman and former professional basketball player.
                      

Another change that was made from Assignment 3 is that methods were split up into their own classes. For example, the pos tagging methods have their own file, translate has its own file, etc. This was implemented after the TA mentioned in our A2 feedback that all our code should not be in one large file. Further code commenting was added to each file to try and make the code and clear as possible.
