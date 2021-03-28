# absolute_randomness
The project is about generating random numbers in real time with the help of data from the Blockchain.
Awarding people randomly from a group of participants: This program help you to select the winner randomly from one of the participants and the outcome cannot be predicted in advance before the enterred date-time.
Use this program to ensure fairness of the contest and the share the code with the participants along with the input before running this program so that they can verify the same.

#Main_Idea
Blockchain Mining is one of the most computationally expensive work where miners try to find the nonce value for the block. The nonce value is number which when added to the block and hashed meets the difficulty requirements. The miners compete to find this nonce value and the first one to do so is rewarded with cryptocurrency of that blockchain.
We are going to use this nonce value of the blocks mined at the time of execution of the program as a seed value for randomness. For more randomness, the program will continue execution till some blocks are mined and all the nonce values are used for randomness.

The randomify.py program uses nonce value of 100 Ethereum blocks which will be mined just after the entered date-time. So, if the date-time entered is of future, it will not be possible to predict the output. The run time of the program is around 25 minutes. So, the program will randomly select one of the participants as winner after about 25 minutes from the date-time entered in the program(Provided it is of future value)

Thus, it is possible to select random winner for any contest publicly - One just need to share the list of participants and the date-time with the public. It won't be possible to predict the outcome before the provided date-time. This way the participants can also verify the fairness of the contest.
