package com.example.practice

import androidx.room.Database
import androidx.room.RoomDatabase

@Database(entities = arrayOf(MyText::class), version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun textDao(): TextDao
}
