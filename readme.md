A python script for making anki cloze.

input:
I {{c1::took a shortcut}} through the university campus.<hr>我抄近路穿过大学校园。
{{c2::Take a shortcut}} for the next task or play normally.<hr>走下一个任务的捷径或正常玩。
You never {{c3::taken a shortcut}} before?<hr>你以前从来没有走过捷径吗？
At some point , the teen decided to {{c4::take a shortcut}} .<hr>在某个时刻，这位青少年决定走一条捷径。
NOTE: You can {{c5::take a shortcut}} here if you like.<hr>注意：如果您愿意，可以在此处走捷径。
And you should never {{c6::take a shortcut}} by pouring it down the drain!<hr>而且你绝对不应该走捷径，把它倒进下水道！
So the Upanishad takes a shortcut .<hr>所以奥义书走了一条捷径。

---------------------------------------------------------
output:
#separator:tab
#html:true
#tags column:2
I {{c1::took}} {{c1::a}} {{c1::shortcut}} through the university campus.<hr>我抄近路穿过大学校园。
{{c1::Take}} {{c1::a}} {{c1::shortcut}} for the next task or play normally.<hr>走下一个任务的捷径或正常玩。
You never {{c1::taken}} {{c1::a}} {{c1::shortcut}} before?<hr>你以前从来没有走过捷径吗？
At some point , the teen decided to {{c1::take}} {{c1::a}} {{c1::shortcut}} .<hr>在某个时刻，这位青少年决定走一条捷径。
NOTE: You can {{c1::take}} {{c1::a}} {{c1::shortcut}} here if you like.<hr>注意：如果您愿意，可以在此处走捷径。
And you should never {{c1::take}} {{c1::a}} {{c1::shortcut}} by pouring it down the drain!<hr>而且你绝对不应该走捷径，把它倒进下水道！
So the Upanishad takes a shortcut .<hr>所以奥义书走了一条捷径。