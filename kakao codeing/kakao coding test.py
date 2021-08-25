# URL = 'https://www.welcomekakao.com/learn/courses/30/lessons/42576?language=python3'


def solution(participant, completion):
    run = participant
    goodrun = completion

    for i in goodrun:
        run.remove(i)
        answer = run
    return answer

answer = solution(["mislav", "stanko", "mislav", "ana"]	, ["stanko", "ana", "mislav"])

#예제1
#["leo", "kiki", "eden"] , ["eden", "kiki"]
print(f"{answer}는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.")

#예제2
#["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]
print(f"{answer} 는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.")

#예제3
# ["mislav", "stanko", "mislav", "ana"]	, ["stanko", "ana", "mislav"]
print(f"{answer} 는 참여자 명단에는 두명이 있지만 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.")
