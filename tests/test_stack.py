from stack import Stack

def test_isEmpty_when_empty() -> None:
	stack = Stack()
	assert stack.isEmpty() == True

def test_pop_from_empty() -> None:
	stack = Stack()
	assert stack.pop() is None

def test_isEmpty_after_push() -> None:
	ARB_VALUE = 7
	stack = Stack()

	stack.push(ARB_VALUE)
	assert stack.isEmpty() == False

def test_pop_after_push() -> None:
	ARB_VALUE = 7
	stack = Stack()

	stack.push(ARB_VALUE)
	assert stack.pop() == ARB_VALUE

def test_filo() -> None:
	ARB_VALUE_1 = 7
	ARB_VALUE_2 = 9

	stack = Stack()

	stack.push(ARB_VALUE_1)
	stack.push(ARB_VALUE_2)

	assert stack.pop() == ARB_VALUE_2
	assert stack.pop() == ARB_VALUE_1
	assert stack.pop() is None

def test_peek_when_empty() -> None:
	stack = Stack()
	assert stack.peek() is None

def test_peek_after_1_push() -> None:
	ARB_VALUE = 7
	stack = Stack()
	stack.push(ARB_VALUE)
	assert stack.peek() == ARB_VALUE
	assert stack.peek() == ARB_VALUE

def test_size_when_empty() -> None:
	assert Stack().size() == 0

def test_size_after_one_push() -> None:
	ARB_VALUE = 7
	stack = Stack()
	stack.push(ARB_VALUE)
	assert stack.size() == 1

def test_size_after_two_pushes() -> None:
	ARB_VALUE_1 = 7
	ARB_VALUE_2 = 9

	stack = Stack()

	stack.push(ARB_VALUE_1)
	stack.push(ARB_VALUE_2)

	assert stack.size() == 2

def test_size_after_three_pushes() -> None:
	ARB_VALUE_1 = 7
	ARB_VALUE_2 = 9
	ARB_VALUE_3 = 11

	stack = Stack()

	stack.push(ARB_VALUE_1)
	stack.push(ARB_VALUE_2)
	stack.push(ARB_VALUE_3)

	assert stack.size() == 3
