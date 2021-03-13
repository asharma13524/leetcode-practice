class Solution:
    def numTrees(self, n: int):
        # numTree[4] = numTree[0] * numTree[3] +
        #              numTree[1] * numTree[2] +
        #              numTree[2] * numTree[1] +
        #              numTree[3] * numTree[0]
        numTree = [1] * (n + 1) # for base cases

        # 0 nodes = 1 tree
        # 1 nodes = 1 tree
        # can start at 2 since base cases are handled
        for nodes in range(2, n + 1):
            # initialize total to 0
            total = 0
            # for all the nodes needed to be placed
            for root in range(1, nodes + 1):
                # left = the root - 1
                left = root - 1
                # right = the num of nodes - root
                right = nodes - root
                # total = left * right to get combinations
                total += numTree[left] * numTree[right]
            numTree[nodes] = total
        return numTree[n]