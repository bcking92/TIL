package com.example.practice

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity
data class MyText(
    @PrimaryKey val uid: Int,
    @ColumnInfo(name = "my_text") val my_text: String?

)
