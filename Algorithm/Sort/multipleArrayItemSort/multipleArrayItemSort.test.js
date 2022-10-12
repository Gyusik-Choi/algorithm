import {describe, expect, it } from '@jest/globals'
import sortCallBack from './multipleArrayItemSort';

describe('sort multiple array items', () => {
  describe('different number of items', () => {
    it('[[1, 1, 3], [1, 1]]', () => {
      const arr = [[1, 1, 3], [1, 1]];
      expect(arr.sort(sortCallBack)).toStrictEqual([[1, 1], [1, 1, 3]]);
    });

    it('[[1, 2], [1, 2, 3]]', () => {
      const arr = [[1, 2], [1, 2, 3]];
      expect(arr.sort(sortCallBack)).toStrictEqual([[1, 2], [1, 2, 3]]);
    });

    it('[[1, 3], [1, 2, 3, 4], [2]]', () => {
      const arr = [[1, 3], [1, 2, 3, 4], [2]];
      expect(arr.sort(sortCallBack)).toStrictEqual([[1, 2, 3, 4], [1, 3], [2]]);
    });

    it('[[1, 2], [2, 2], [2], [2, 1], [9]]', () => {
      const arr = [[1, 2], [2, 2], [2], [2, 1], [9]];
      expect(arr.sort(sortCallBack)).toStrictEqual([[1, 2], [2], [2, 1], [2, 2], [9]]);
    });
  });

  describe('same number of items', () => {
    it('[[1, 1, 3], [1, 1, 2], [1, 1, 1], [1, 1, 4]]', () => {
      const arr = [[1, 1, 3], [1, 1, 2], [1, 1, 1], [1, 1, 4]];
      expect(arr.sort(sortCallBack)[0]).toStrictEqual([1, 1, 1]);
    })
  })
});

// https://poiemaweb.com/jest-esm
