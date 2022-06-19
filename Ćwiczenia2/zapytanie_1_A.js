printjson(db.people.aggregate(
    [{$group: {
        _id: '$sex',
        totalWeight: { $sum: '$weight' },
        totalHeight: { $sum: '$height' },
        total_elements: { $sum: 1 }
    }},
    {$project: {
        averWeight: {
            $divide: ['$totalWeight', '$total_elements']
        },
        averHeight: {
            $divide: ['$totalHeight', '$total_elements']
        }
    }}
]).toArray())