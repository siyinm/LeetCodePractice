Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

### Solution

中序遍历的过程中，若有不符合升序条件的，记录节点，

有一处不符合，则交换那两个节点的val

有两处不符合，交换两个节点的valse

New a pointer to restore the previous treenode while traversing.