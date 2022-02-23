# Another approach based on dislikes. 

Sort the candidates based on the number of dislikes.

Take the initial guess of the ingredient list to be the list of the liked elements from the first client in this sorted client list, i.e., the client with the least number of dislikes.

Iterate over the other clients and if none of the dislikes of the client under consideration occur in our ingredient list, add its like list to our ingredient list.

Gives best results for c_coarse.in.txt and e_elaborate.in.txt.
