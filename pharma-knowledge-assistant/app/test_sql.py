from services.sql_generator import generate_sql
from services.sql_executor import execute_sql
from services.sql_answer_generator import generate_sql_answer

question = "What are Brintellix sales in India?"

sql = generate_sql(question)

print("Generated SQL:")
print(sql)

result = execute_sql(sql)

print("\nRaw Result:")
print(result)

answer = generate_sql_answer(
    question,
    sql,
    result
)

print("\nFinal Answer:")
print(answer)