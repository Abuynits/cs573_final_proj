import matplotlib.pyplot as plt
import numpy as np
import re
def generate_stacked_bar_graph(df, variable_map):
    fig, ax = plt.subplots(figsize=(10, 8))
    categories = df['Course'].unique()
    drop_counts = []
    graduate_counts = []
    for degree in categories:
        count_entries = df[df['Course'] == degree]['dropout'].value_counts()
        drop_counts.append(count_entries["Dropout"])
        graduate_counts.append(count_entries["Graduate"])

    categories = [variable_map["Course"][course] for course in variable_map["Course"]]
    ax.set_xticks(range(len(categories)))
    ax.set_xticklabels(categories, rotation=45, ha='right')
    plt.bar(categories, drop_counts, color='r', label="dropout")
    plt.bar(categories, graduate_counts, bottom=drop_counts, color='b', label="graduate")

    ax.set_ylabel('Students')
    ax.set_title('Graduation vs Dropout Rates of Students')
    ax.legend()
    plt.show()

def jitter_plot(df):
    plt.figure(figsize=(10, 6))
    PREV_QUAL = 'Previous qualification (grade)'
    ADMISSION_GRADE = 'Admission grade'
    # adding jitter to elements to prevent repeats:
    dropout_prev_qual = df[PREV_QUAL][df['dropout'] == 'Dropout'].to_numpy()
    dropout_prev_score = df[ADMISSION_GRADE][df['dropout'] == 'Dropout'].to_numpy()
    jitter = 0.25 * np.random.randn(dropout_prev_score.shape[0])
    dropout_prev_qual += jitter
    dropout_prev_score += jitter

    plt.scatter(dropout_prev_qual, dropout_prev_score, color='red', label='Dropout')

    graduate_prev_qual = df[PREV_QUAL][df['dropout'] == 'Graduate']
    graduate_prev_score = df[ADMISSION_GRADE][df['dropout'] == 'Graduate']
    jitter = 0.25 * np.random.randn(graduate_prev_score.shape[0])
    graduate_prev_score += jitter
    graduate_prev_qual += jitter

    plt.scatter(graduate_prev_qual, graduate_prev_score, color='blue', label='Graduate')

    plt.xlabel('Past Grades')
    plt.ylabel('Admission Score')
    plt.legend()
    plt.title('Comparison between Admission Scores and Grades vs Dropout')
    plt.grid(True)
    plt.show()

def pie_chart(y_col):
    unique, counts = np.unique(y_col, return_counts=True)
    plt.figure(figsize=(4, 4))
    plt.pie(counts, labels=unique, autopct=lambda p: '{:.1f}% ({:.0f})'.format(p, (p / 100) * sum(counts)))
    plt.title('Dropout Pie chart')
    plt.axis('equal')
    plt.show()

def plot_semester_compare_bp(df, curriculum_units):

    plot_df = df[list(curriculum_units)]
    clean_text = lambda x: re.sub(r'(Curricular units |\(|\))', '', x)
    desired_order = [clean_text(x) for x in curriculum_units]
    pairs = [(desired_order[i], desired_order[i + 1]) for i in range(0, len(desired_order), 2)]
    plot_df = plot_df.rename(columns={x: clean_text(x) for x in curriculum_units})
    # plot_df.boxplot(vert=False)

    fig, axes = plt.subplots(len(pairs), 1, figsize=(10, 12))
    fig.subplots_adjust(hspace=0.5)

    for i, ax in enumerate(axes):
        renamed_df = plot_df.copy().rename(columns={x: " ".join(x.split()[:2]) for x in pairs[i]})
        renamed_df[['1st sem', '2nd sem']].boxplot(vert=False, ax=ax)
        title = " ".join(pairs[i][0].split()[2:])
        ax.set_title(f"{title} Curricular units between 1st and 2nd sem")
        # ax.set_yticklabels("units", rotation=45, ha='right')
        for j, column in enumerate(['1st sem', '2nd sem']):
            q1 = renamed_df[column].quantile(0.25)
            median = renamed_df[column].median()
            q3 = renamed_df[column].quantile(0.75)

            y_pos = j + 1
            all_summary = f'Q1: {q1:.2f} | Median: {median:.2f} | Q3: {q3:.2f}'
            ax.text(median, y_pos + 0.4, all_summary, verticalalignment='top', color='red', fontsize=9)

    fig.suptitle("Curricular Units between 1st and 2nd Semester", fontsize=16)

    plt.show()