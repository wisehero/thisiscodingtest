"""
[from , to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라.
여러 일정이 있는 경우 사전 어휘 순으로 방문한다.

Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
"""
import collections


def findItinerary(self, tickets):
    graph = collections.defaultdict(list)
    # 그래프를 뒤집어서 구성
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []

    def dfs(a):
        # 마지막 값을 읽어 어휘 순 방문
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)

    dfs('JFK')
    # 다시 뒤집어 어휘 순 결과로
    return route[::-1]


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

print(findItinerary(tickets))
