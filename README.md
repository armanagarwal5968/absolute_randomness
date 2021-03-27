# absolute_randomness
The project is about generating random numbers in real time with the help[ of data from the Blockchain.

#Main_Idea
Blockchain Mining is one of the most computationally expensive work where miners try to find the nonce value for the block. The nonce value is number which when added to the block and hashed meets the difficulty requirements. The miners compete to find this nonce value and the first one to do so is rewarded with cryptocurrency of that blockchain.
We are going to use this nonce value of the blocks mined at the time of execution of the program as a seed value for randomness. For more randomness, the program will continue execution till some blocks are mined and all the nonce values are used for randomness.

