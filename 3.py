N = int(input())
A = list(map(int, input().split()))

count = {}

for k in A:
    if k in count:
        count[k] += 1
    else:
        count[k] = 1
    
answer_name = -1
answer_atai = -1

for name, atai in count.items():
    if answer_atai < atai:
        answer_name = name
        answer_atai = atai
    elif answer_atai == atai and answer_name > name:
        answer_name = name
        answer_atai = atai
    
print(answer_name, answer_atai)
print(count)
print(len(count))

#入力
#20
#1 4 2 3 5 3 2 4 2 6 8 7 6 4 5 6 4 3 5 2 
#に対し出力
#2 4
#{1: 1, 4: 4, 2: 4, 3: 3, 5: 3, 6: 3, 8: 1, 7: 1}
#8