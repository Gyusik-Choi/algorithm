import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class ReorderDataInLogFiles937_4 {
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

        List<String> sortedLetters = letters
                .stream()
                .map(Log4::new)
                .sorted()
                .map(Log4::getLog)
                .collect(Collectors.toList());

        sortedLetters.addAll(digits);
        return sortedLetters.toArray(new String[0]);
    }

    private boolean isDigitOnly(String log) {
        return Character.isDigit(log.split(" ")[1].charAt(0));
    }
}

class Log4 implements Comparable<Log> {
    private final String log;
    private String identifier;
    private String words;

    Log4(String log) {
        this.log = log;
        splitLog();
    }

    public String getLog() {
        return log;
    }

    public String getIdentifier() {
        return identifier;
    }

    public String getWords() {
        return words;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public void setWords(String words) {
        this.words = words;
    }

    private void splitLog() {
        String[] logList = log.split(" ", 2);
        setIdentifier(logList[0]);
        setWords(logList[1]);
    }

    @Override
    public int compareTo(Log o) {
        if (this.getWords().compareTo(o.getWords()) == 0) {
            return this.getIdentifier().compareTo(o.getIdentifier());
        }
        return this.getWords().compareTo(o.getWords());
    }
}