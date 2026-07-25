package com.example

class QueueReconstructionByHeight406_3 {
    fun reconstructQueue(people: Array<IntArray>): Array<IntArray> {
        val sortedPeople = people.sortedArrayWith { a, b -> if (a[0] == b[0]) a[1] - b[1] else b[0] - a[0] }
        val list = mutableListOf<IntArray>()
        for (person in sortedPeople) {
            if (list.size <= person[1]) {
                list.add(person)
            } else {
                list.add(person[1], person)
            }
        }
        return list.toTypedArray()
    }
}
