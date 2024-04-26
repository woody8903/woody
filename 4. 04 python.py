def count_sums(N): #def- 함수를 정의하는 키워드, 함수를 선언할때 사용. count_sums - 함수의 이름. 연속된 숫자의 합이 총 몇개인지 새는것. 
    count = 0 #위의 함수 결과 갯수를 저장하는 변수.

    for start in range(1, N + 1): # 1부터 N까지의 숫자에 대해 반복하면서 연속된 자연수의 합을 구하는 작업.
        sum = 0 #그 값을 저장.
        for current in range(start, N + 1): # 1부터 start까지의 숫자에 대해서 반복 하면서, 각 숫자를 이전까지의 합에 더하는 작업을 수행.
            sum += current #이를 통해 연속된 자연수의 합을 구할 수 있다.
            if sum == N: #뭐 더하기 뭐가 N값이랑 같으면 갯수 저장.
                count += 1 
            elif sum > N: #예를들어 10은 1+2+3+4인데 안에 들어갈 숫자가 10을 넘으면 중단.
                break

    return count # 위의 결과를 가지고와서 밑으로 전달.

N = int(input("자연수 N을 입력하세요: "))

print("자연수", N, "을 연속된 자연수 합으로 나타내는 가짓수는", count_sums(N), "개 입니다.")

