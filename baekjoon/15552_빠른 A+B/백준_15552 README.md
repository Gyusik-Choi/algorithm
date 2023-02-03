# 백준

## 15552

-  BufferedReader
   -  Scanner 보다 효율이 높다. 입력이 많거나 효율성 체크를 하는 문제에서는 Scanner 사용은 지양하고 BufferedReader 사용을 지향해야 한다. Scanner와 달리 공백 외에 한 줄 단위로만 읽고, 읽은 데이터는 String이 된다. 정수 값으로 활용하려면 정수로 변환하는 과정이 필요하며, 공백이 있을 경우 공백을 구분해주는 과정이 필요하다.
-  BufferedWriter
   -  System.out.println() 처럼 출력을 해주는 함수이나 효율 면에서 더 우수하다. 차이는 개행을 해주지 않기 때문에 개행이 필요하면 추가적으로 개행을 위한 코드를 넣어야 한다. 
   -  개행을 하려면 BufferedWriter의 변수를 bw로 했을 경우, bw.newLine();을 출력마다 추가하거나, bw.write(출력할 내용 + "\n")을 통해 개행할 수 있다. 
-  flush(), close() 메서드를 출력을 마친 후 꼭 호출해야 한다.
   
-  StringTokenizer: 지정된 구분자를 통해 문자열을 나눈다.
