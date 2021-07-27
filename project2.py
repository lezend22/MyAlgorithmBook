import heapq

def dijkstra(graph, first):
    distance = {node:float('inf') for node in graph}
    distance[first] = 0 # 첫 번째 노드거리 0
    queue = []
    heapq.heappush(queue, [distance[first], first]) # 우선순위 큐에 첫번째 값 넣어줌

    # queue에 데이터 없을 때 까지 반복
    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distance[current_node] < current_distance: # 우선순위 큐의 값이 더 클경우 반복문 실행할 필요 없음
            continue

        for next_node, weight in graph[current_node].items():
            total_distance = current_distance + weight

            if total_distance < distance[next_node]:
                distance[next_node] = total_distance
                heapq.heappush(queue, [total_distance, next_node])

    return distance

graph = {
    'A': {'B':50},
    'B':{'A':50, 'C':35, 'D':140},
    'C':{'B':35, 'E':150, 'F':140},
    'D':{'B':140, 'E':55},
    'E':{'D':55, 'C':150, 'G': 55},
    'F':{'C':140, 'G':60, 'H':100},
    'G':{'E':55, 'F':60, 'J':170},
    'H':{'F':100, 'I':55},
    'I':{'H':55, 'J':30},
    'J':{'G':170, 'I':30, 'K':15},
    'K':{'J':15}
}

if __name__ == '__main__':
    print(dijkstra(graph, 'A'))