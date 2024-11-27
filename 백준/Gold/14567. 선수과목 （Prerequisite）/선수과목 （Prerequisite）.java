/*

위상정렬
list를 [] 안에 ArrayList를 받는 이차원 형태로 선언한다
list[a].add[x]로 a -> x로 향하는 관계를 나타낸다
진입차수를 다루는 배열도 추가로 선언해준다
q에는 진입차수가 0인 점들을 q에 오퍼한다
모든 배열을 순회하는지 여부를 확인하는 int 변수도 만든다
while(모든 노드를 순회하지 않았으며 q가 비어있지 않을 때)
    q 크기만큼 반복문을 돌린다(위상정렬은 시작지점이 정해져 있지 않다)
    현 지점에서 다음 지점으로 가며 진출차수를 하나 낮춘다
    다음지점이 진출차수가 0이 된다면 새로운 큐로 오퍼한다
여긴 루프를 잘 순회한 경우이므로 cnt++
if(visitCnt가 n이라면 값 출력)
else면 -1
 */

import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 과목의 수
        int M = Integer.parseInt(st.nextToken()); // 선수 조건의 수

        List<Integer>[] graph = new ArrayList[N + 1]; // 이차원 배열인데 내부는 arraylist로
        int[] inDegree = new int[N + 1]; // 진입차수 배열
        int[] semesterRequired = new int[N + 1]; // 선수과목으로 이수해야하는 최소 학기 수

        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>(); // 배열 초기화
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken()); // A -> B
            graph[A].add(B);
            inDegree[B]++; // 진입차수++
        }

        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            if (inDegree[i] == 0) {
                q.offer(i); // 진입차수 0인점 오퍼
                semesterRequired[i] = 1; // 선수과목 없으므로 1
            }
        }

        while (!q.isEmpty()) {
            int current = q.poll();

            for (int next : graph[current]) { // graph[current]에는 현재 갈 수 있는 진출차수가 ArrayList형태로 선언되어있다
                inDegree[next]--; //
                if (inDegree[next] == 0) {
                    q.offer(next); // 사이클없이 간선을 다 제거하는데 성공했으면 그 지점에서 다시 시작
                    semesterRequired[next] = semesterRequired[current] + 1; // 선수과목 학기 수++
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            sb.append(semesterRequired[i]).append(" "); // 선수과목 필요한 학기들 출력
        }

        System.out.println(sb);
    }
}