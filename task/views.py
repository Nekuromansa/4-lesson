from django.http import HttpResponse
from django.shortcuts import redirect

tasks = [
    {
        'name': 'Hisobot tayyorlash',
        'description': 'Oylik moliyaviy hisobotni tayyorlash va topshirish',
        'priority': 'Yuqori',
        'due_date': '2023-05-31',
        'status': 'Bajarilmoqda'
    },
    {
        'name': 'Mijoz bilan uchrashuv',
        'description': 'Yangi loyiha bo‘yicha mijoz bilan muzokaralar o‘tkazish',
        'priority': 'O‘rta',
        'due_date': '2023-05-25',
        'status': 'Rejalashtirilgan'
    },
    {
        'name': 'Prezentatsiya tayyorlash',
        'description': 'Yangi mahsulot uchun taqdimot slaydlarini tayyorlash',
        'priority': 'Past',
        'due_date': '2023-06-05',
        'status': 'Boshlanmagan'
    },
    {
        'name': 'Xodimlar uchun trening',
        'description': 'Yangi dasturiy ta’minot bo‘yicha xodimlarga qo‘llanma berish',
        'priority': 'O‘rta',
        'due_date': '2023-06-10',
        'status': 'Rejalashtirilgan'
    },
    {
        'name': 'Loyiha hujjatlarini yangilash',
        'description': 'Joriy loyihaning texnik hujjatlarini yangilash va arxivlash',
        'priority': 'Past',
        'due_date': '2023-06-15',
        'status': 'Boshlanmagan'
    }
]

def task_list_view(request):
    global tasks

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')

        if name and priority and due_date:
            task = {
                'name': name,
                'description': description,
                'priority': priority,
                'due_date': due_date,
                'status': 'Boshlanmagan'
            }
            tasks.append(task)
            return redirect('/')

    html = """
    <!DOCTYPE html>
    <html lang="uz">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Vazifalar Ro‘yxati</title>
        <style>
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { border: 1px solid #000; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            form { margin-bottom: 20px; }
            input, select, textarea { display: block; margin: 10px 0; width: 100%; max-width: 400px; padding: 5px; }
        </style>
    </head>
    <body>
        <h1>Vazifalar Ro‘yxati</h1>

        <h2>Yangi vazifa qo‘shish</h2>
        <form method="post">
            """ + f"""
            <input type="hidden" name="csrfmiddlewaretoken" value="{request.COOKIES.get('csrftoken')}">
            """ + """
            <label for="name">Vazifa nomi:</label>
            <input type="text" id="name" name="name" required>

            <label for="description">Tavsif:</label>
            <textarea id="description" name="description"></textarea>

            <label for="priority">Muhimlik darajasi:</label>
            <select id="priority" name="priority" required>
                <option value="Past">Past</option>
                <option value="O‘rta">O‘rta</option>
                <option value="Yuqori">Yuqori</option>
            </select>

            <label for="due_date">Muddat:</label>
            <input type="date" id="due_date" name="due_date" required>

            <button type="submit">Vazifani qo‘shish</button>
        </form>

        <h2>Mavjud vazifalar</h2>
        <table>
            <thead>
                <tr>
                    <th>Vazifa</th>
                    <th>Tavsif</th>
                    <th>Muhimlik</th>
                    <th>Muddat</th>
                    <th>Holat</th>
                </tr>
            </thead>
            <tbody>
    """

    if tasks:
        for task in tasks:
            html += f"""
                <tr>
                    <td>{task['name']}</td>
                    <td>{task['description']}</td>
                    <td>{task['priority']}</td>
                    <td>{task['due_date']}</td>
                    <td>{task['status']}</td>
                </tr>
            """
    else:
        html += """
            <tr>
                <td colspan="5">Hozircha vazifalar yo‘q</td>
            </tr>
        """

    html += """
            </tbody>
        </table>
    </body>
    </html>
    """

    return HttpResponse(html)
