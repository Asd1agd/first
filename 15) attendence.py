def attendance(names):
    first_names = [name.split()[0] for name in names]
    name_count = {name: first_names.count(name) for name in first_names}
    for name in names:
        if name_count[name.split()[0]] > 1:
            print(name)
        else:
            print(name.split()[0])

# Example usage:
names = ['John Doe', 'Jane Smith', 'Michael Johnson', 'Jane Lee', 'Emily Jones', 'Michael Williams']
attendance(names)
