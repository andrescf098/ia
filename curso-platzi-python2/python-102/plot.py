import matplotlib.pyplot as plt

def generate_bar_char(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    labels = ['A', 'B', 'C']
    values = [1, 4, 2]
    generate_pie_chart(labels, values)