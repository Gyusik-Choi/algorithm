import java.util.ArrayList;
import java.util.List;

public class ReorderDataInLogFiles937_2 {
    public String[] reorderLogFiles(String[] logs) {
        List<String> digits = new ArrayList<>();
        List<String> letters = new ArrayList<>();

        for (String log : logs) {
            if (isDigitOnly(log)) {
                digits.add(log);
            } else {
                letters.add(log);
            }
        }

        letters.sort((first, second) -> {
            String[] firstWords = first.split(" ", 2);
            String[] secondWords = second.split(" ", 2);

            if (firstWords[1].compareTo(secondWords[1]) == 0) {
                return firstWords[0].compareTo(secondWords[0]);
            }
            return firstWords[1].compareTo(secondWords[1]);
        });

        letters.addAll(digits);
        return letters.toArray(new String[0]);
    }

    private boolean isDigitOnly(String log) {
        String[] words = log.split(" ", 2);
        return words[1]
                .replaceAll("^[\\s0-9]+", "")
                .isEmpty();
    }
}
