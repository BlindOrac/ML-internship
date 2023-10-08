training_data = [['Green', 3, 'Mango'],
                 ['Yellow', 3, 'Mango'],
                 ['Red', 1, 'Grape'],
                 ['Red', 1, 'Grape'],
                 ['Yellow', 3, 'Lemon']]

header = ["color", "diameter", "label"]


def unique_vals(rows, col):
    return set([row[col] for row in rows])


print(unique_vals(training_data, 0))
print(unique_vals(training_data, 1))


def class_counts(rows):
    counts = {}
    for row in rows:
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts


print(class_counts(training_data))


def is_numeric(value):
    return isinstance(value, int) or isinstance(value, float)


class Question:

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        condition = "=="
        if is_numeric(self.value):
            condition = ">="
        return "Is %s %s %s" % (header[self.column], condition, str(self.value))


def partition(rows, question):
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows


true_rows, false_rows = partition(training_data, Question(0, 'Red'))
print(true_rows)
print(false_rows)


def gini(rows):
    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl ** 2
    return impurity


print(gini(training_data))


def info_gain(left, right, current_uncertainty):
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)


current_uncertainty = gini(training_data)
print("Current incertainty:", current_uncertainty)

true_rows1, false_rows1 = partition(training_data, Question(0, 'Red'))
print(info_gain(true_rows1, false_rows1, current_uncertainty))

true_rows2, false_rows2 = partition(training_data, Question(0, 'Green'))
print(info_gain(true_rows2, false_rows2, current_uncertainty))


def find_best_split(rows):
    best_gain = 0
    best_question = None
    current_uncertainty = gini(rows)
    n_of_features = len(rows[0]) - 1

    for col in range(n_of_features):
        values = set([row[col] for row in rows])

        for val in values:
            question = Question(col, val)

            true_rows, false_rows = partition(rows, question)

            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            gain = info_gain(true_rows, false_rows, current_uncertainty)

            if gain >= best_gain:
                best_gain, best_question = gain, question
    return best_gain, best_question


best_gain1, best_question1 = find_best_split(training_data)
print(best_gain1)
print(best_question1)


class Leaf:

    def __init__(self, rows):
        self.predictions = class_counts(rows)


class Decision_Node:

    def __init__(self,
                 question,
                 true_branch,
                 false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch


def build_tree(rows):
    gain, question = find_best_split(rows)

    if gain == 0:
        return Leaf(rows)

    true_rows3, false_rows3 = partition(rows, question)

    true_branch = build_tree(true_rows3)
    false_branch = build_tree(false_rows3)

    return Decision_Node(question, true_branch, false_branch)


def print_tree(node, spacing=""):
    if isinstance(node, Leaf):
        print(spacing + "Predict", node.predictions)
        return

    print(spacing + str(node.question))

    print(spacing + '--> True:')
    print_tree(node.true_branch, spacing + "  ")

    print(spacing + '--> False:')
    print_tree(node.false_branch, spacing + "  ")


def classify(row, node):
    if isinstance(node, Leaf):
        return node.predictions

    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)


my_tree = build_tree(training_data)
print(classify(training_data[0], my_tree))


def print_leaf(counts):
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs

print(print_leaf(classify(training_data[0], my_tree)))
print_tree(my_tree)