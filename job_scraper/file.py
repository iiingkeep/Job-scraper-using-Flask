def save_to_file(file_name, jobs):
  file = open(f"{file_name}.csv", "w", encoding="utf-8", newline = "")
  file.write('Title, Company, Location, Salary, URL\n')

  for job in jobs:
    file.write(
      f"{job['title']}, {job['company']}, {job['location']},{job['salary']}, {job['url']}\n"
    )

  file.close()

