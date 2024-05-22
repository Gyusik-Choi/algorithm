input = '5\n2 3 1 2 2';

input = input.split('\n');
N = parseInt(input[0]);
adventurers = input[1].split(' ').map(v => parseInt(v))
adventurers.sort((a, b) => a - b);

max_group_cnt = 0;
cnt = 0;

for (const adventurer of adventurers) {
  cnt += 1;

  if (adventurer !== cnt) {
    continue;
  }

  max_group_cnt += 1;
  cnt = 0;
}

console.log(max_group_cnt);
