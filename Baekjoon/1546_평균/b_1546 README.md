# 백준

## 1546

```java
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(br.readLine());

		double sums = 0.0;
		int max = 0;
		
		for (int i = 0; i < N; i++) {
			int grade = Integer.parseInt(st.nextToken());
			if (grade > max) {
				max = grade;
			}
			sums += grade;
		}
```



```java
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		double sums = 0.0;
		int max = 0;
		
		for (int i = 0; i < N; i++) {
			int grade = Integer.parseInt(st.nextToken());
			if (grade > max) {
				max = grade;
			}
			sums += grade;
		}
```

위와 아래는 StringTokenizer의 선언부의 위치가 다르다. 

N은 StringTokenizer의 사용이 필요가 없이 1개의 숫자만 받는다. N보다 먼저 StringTokenizer를 선언하면 N을 제대로 입력받지 못하고 오류가 발생한다.

N을 먼저 입력 받은 후에 StringTokenizer를 선언해야 오류를 피할 수 있다.