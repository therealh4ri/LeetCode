class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split('/')

        for component in components:
            if component == '' or component == '.':
                continue
            elif component == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(component)

        # Construct the simplified canonical path
        canonical_path = '/' + '/'.join(stack)

        return canonical_path

        