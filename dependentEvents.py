from independentEvents import probability

box1 = {'black': 3, 'white': 4}

box2_if_whiteFrom1 = {'white': 4, 'black': 5}
box2_if_blackFrom1 = {'white': 3, 'black': 6}

blackFromBox2 = (probability(['black'], box1)*probability(['black'], box2_if_blackFrom1))+(probability(['white'], box1)*probability(['black'], box2_if_whiteFrom1))
whiteFromBox2 = 1-blackFromBox2

whiteFromBox1_if_whiteFromBox2 = (probability(['white'], box1)*probability(['white'], box2_if_whiteFrom1))/whiteFromBox2

print(round(blackFromBox2*100, 2), round(whiteFromBox2*100, 2), round(whiteFromBox1_if_whiteFromBox2, 2)*100)