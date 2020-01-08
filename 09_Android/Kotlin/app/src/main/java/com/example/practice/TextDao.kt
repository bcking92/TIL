package com.example.practice

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.Query

@Dao
interface TextDao {
    @Query("SELECT * FROM mytext")
    fun getAll(): List<MyText>

    @Query("SELECT * FROM mytext WHERE uid IN (:userIds)")
    fun loadAllByIds(userIds: IntArray): List<MyText>

    @Query("SELECT * FROM user WHERE first_name LIKE :first AND " +
            "last_name LIKE :last LIMIT 1")
    fun findByName(first: String, last: String): MyText

    @Insert
    fun insertAll(vararg users: MyText)

    @Delete
    fun delete(user: MyText)
}
