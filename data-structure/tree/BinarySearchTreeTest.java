import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.assertj.core.api.Assertions.*;

class BinarySearchTreeTest {

    private BinarySearchTree bst;

    @BeforeEach
    void setUp() {
        bst = new BinarySearchTree();
    }

    @Test
    @DisplayName("이진탐색트리가 비었을 경우 true 를 반환한다")
    void isEmpty1() {
        assertThat(bst.isEmpty()).isTrue();
    }

    @Test
    @DisplayName("이진탐색트리가 비어있지 않을 경우 false 를 반환한다")
    void isEmpty2() {
        bst.add(1);
        assertThat(bst.isEmpty()).isFalse();
    }

    @Test
    @DisplayName("이진탐색트리가 비었을 경우 조회 결과는 false 다")
    void search1() {
        assertThat(bst.search(1)).isFalse();
    }

    @Test
    @DisplayName("이진탐색트리에 1이 있고 1을 조회할 경우 true 를 반환한다")
    void search2() {
        bst.add(1);
        assertThat(bst.search(1)).isTrue();
    }

    @Test
    @DisplayName("이진탐색트리에 있는 노드만 조회하고 없는 노드는 조회되지 않는다")
    void search3() {
        bst.add(4);
        bst.add(2);
        bst.add(3);
        bst.add(1);
        bst.add(5);
        assertThat(bst.search(1)).isTrue();
        assertThat(bst.search(2)).isTrue();
        assertThat(bst.search(3)).isTrue();
        assertThat(bst.search(4)).isTrue();
        assertThat(bst.search(5)).isTrue();
        assertThat(bst.search(6)).isFalse();
    }

    @Test
    @DisplayName("이진탐색트리가 비었을 경우 삭제 결과는 false 다")
    void remove1() {
        assertThat(bst.remove(1)).isFalse();
    }

    @Test
    @DisplayName("이진탐색트리에 1이 있고 1을 삭제하면 true 를 반환한다. " +
            "만약에 삭제한 노드가 유일한 노드였면 이진탐색트리에 존재하는 노드가 없다")
    void remove2() {
        bst.add(1);
        assertThat(bst.remove(1)).isTrue();
        assertThat(bst.isEmpty()).isTrue();
    }

    @Test
    @DisplayName("루트 노드가 왼쪽 자식 노드만 있을 때 루트 노드를 삭제할 경우" +
            "왼쪽 자식 노드가 루트 노드가 된다")
    void remove3() {
        bst.add(3);
        bst.add(1);
        assertThat(bst.remove(3)).isTrue();
        assertThat(bst.search(3)).isFalse();
        assertThat(bst.search(1)).isTrue();
    }

    @Test
    @DisplayName("루트 노드가 왼쪽 자식 노드만 있을 때 왼쪽 자식 노드를 삭제할 경우" +
            "루트 노드만 남는다")
    void remove4() {
        bst.add(3);
        bst.add(1);
        assertThat(bst.remove(1)).isTrue();
        assertThat(bst.search(1)).isFalse();
    }

    @Test
    @DisplayName("루트 노드가 오른쪽 자식 노드만 있을 때 오른쪽 자식 노드를 삭제할 경우" +
            "오른쪽 자식 노드가 루트 노드가 된다")
    void remove5() {
        bst.add(1);
        bst.add(3);
        assertThat(bst.remove(1)).isTrue();
        assertThat(bst.search(1)).isFalse();
        assertThat(bst.search(3)).isTrue();
    }

    @Test
    @DisplayName("루트 노드가 오른쪽 자식 노드만 있을 때 오른쪽 자식 노드를 삭제할 경우" +
            "루트 노드만 남는다")
    void remove6() {
        bst.add(1);
        bst.add(3);
        assertThat(bst.remove(3)).isTrue();
        assertThat(bst.search(3)).isFalse();
    }

    @Test
    @DisplayName("루트 노드가 왼쪽, 오른쪽 자식 노드가 모두 있을 때 루트 노드를 삭제할 경우" +
            "왼쪽, 오른쪽 자식 노드가 모두 남는다")
    void remove7() {
        bst.add(2);
        bst.add(1);
        bst.add(3);
        assertThat(bst.remove(2)).isTrue();
        assertThat(bst.search(1)).isTrue();
        assertThat(bst.search(3)).isTrue();
    }

    @Test
    @DisplayName("왼쪽 자식 노드가 있는 자식 노드를 삭제할 경우 왼쪽 자식 노드가 삭제한 노드의 자리로 온다")
    void remove8() {
        bst.add(3);
        bst.add(2);
        bst.add(1);
        bst.add(4);
        bst.add(5);
        assertThat(bst.remove(2)).isTrue();
        assertThat(bst.search(2)).isFalse();
        assertThat(bst.search(1)).isTrue();
    }

    @Test
    @DisplayName("오른쪽 자식 노드가 있는 자식 노드를 삭제할 경우 오른쪽 자식 노드가 삭제한 노드의 자리로 온다")
    void remove9() {
        bst.add(3);
        bst.add(2);
        bst.add(1);
        bst.add(4);
        bst.add(5);
        assertThat(bst.remove(4)).isTrue();
        assertThat(bst.search(4)).isFalse();
        assertThat(bst.search(5)).isTrue();
    }

    @Test
    @DisplayName("삭제하는 노드의 오른쪽 자식노드가 존재하는 경우 이 자식노드는 제거되면 안 된다")
    void remove10() {
        bst.add(4);
        bst.add(1);
        bst.add(8);
        bst.add(6);
        bst.add(10);
        bst.add(7);
        assertThat(bst.remove(6)).isTrue();
        assertThat(bst.search(6)).isFalse();
        assertThat(bst.search(7)).isTrue();
    }

    @Test
    @DisplayName("왼쪽, 오른쪽 리프 노드를 자식 노드로 둔 자식 노드를 삭제할 경우 " +
            "왼쪽, 오른쪽 리프 노드는 남고 오른쪽 리프 노드가 삭제한 노드의 자리로 온다")
    void remove11() {
        bst.add(4);
        bst.add(2);
        bst.add(1);
        bst.add(6);
        bst.add(5);
        bst.add(7);
        assertThat(bst.remove(6)).isTrue();
        assertThat(bst.search(6)).isFalse();
        assertThat(bst.search(5)).isTrue();
        assertThat(bst.search(7)).isTrue();
    }

    @Test
    @DisplayName("전위 순회")
    void preOrder1() {
        bst.add(4);
        bst.add(2);
        bst.add(1);
        bst.add(3);
        bst.add(6);
        bst.add(5);
        bst.add(7);
        List<Integer> preOrderList = List.of(4, 2, 1, 3, 6, 5, 7);
        assertThat(bst.preOrder()).isEqualTo(preOrderList);
    }

    @Test
    @DisplayName("중위 순회")
    void inOrder1() {
        bst.add(4);
        bst.add(2);
        bst.add(1);
        bst.add(3);
        bst.add(6);
        bst.add(5);
        bst.add(7);
        List<Integer> inOrderList = List.of(1, 2, 3, 4, 5, 6, 7);
        assertThat(bst.inOrder()).isEqualTo(inOrderList);
    }

    @Test
    @DisplayName("후위 순회")
    void postOrder1() {
        bst.add(4);
        bst.add(2);
        bst.add(1);
        bst.add(3);
        bst.add(6);
        bst.add(5);
        bst.add(7);
        List<Integer> postOrderList = List.of(1, 3, 2, 5, 7, 6, 4);
        assertThat(bst.postOrder()).isEqualTo(postOrderList);
    }
}