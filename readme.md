# Транспортна Мережа Київського Метрополітену

## Завдання 1: Створення та візуалізація графу транспортної мережі
### Основні характеристики графу

- **Кількість вершин:** Кількість вершин відповідає кількості станцій метро в Київському метрополітені.
- **Кількість ребер:** Кількість ребер включає зв'язки між станціями на кожній лінії метро, а також пересадки між лініями.
- **Ступінь вершин:** Ступінь кожної вершини визначається кількістю ліній метро, що проходять через відповідну станцію.

## Завдання 2: Використання алгоритмів DFS і BFS для знаходження шляхів у графі

### Порівняння результатів

- **Відмінності в шляхах:** DFS може повернути будь-який з можливих шляхів, не гарантуючи, що він буде найкоротшим. BFS завжди гарантує найкоротший шлях за кількістю ребер.
- **Час виконання:** В загальному випадку, BFS може бути більш оптимальним для знаходження найкоротшого шляху в графах з невеликою глибиною. DFS може виконуватися швидше в графах з великою кількістю гілок, але не гарантує найкоротший шлях.

### Висновок

Алгоритми DFS та BFS мають різні підходи до пошуку шляхів у графі. BFS є оптимальним вибором для знаходження найкоротшого шляху у транспортній мережі, оскільки він гарантує мінімальну кількість пересадок. DFS може бути корисним для дослідження всіх можливих маршрутів, хоча і не завжди знайде найкоротший шлях. Для задач, де важлива оптимальність шляху, BFS є кращим вибором, тоді як DFS може бути використаний для повного дослідження графу.
