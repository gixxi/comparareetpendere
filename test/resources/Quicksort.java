package org.jane;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;

public class Quicksort {
	<T extends Comparable<T>> Collection<T> sort(Collection<T> in) {
		if(in.size() <= 1) return in;
		Iterator<T> iter = in.iterator();
		T separator = iter.next();
		List<T> left = new ArrayList<>();
		List<T> right = new ArrayList<>();
		while(iter.hasNext()) {
			T elem = iter.next();
			if(elem.compareTo(separator) <= 0) left.add(elem);
			else right.add(elem);
		}
		Collection<T> result = sort(left);
		result.add(separator);
		result.addAll(sort(right));
		return result;
	}
	
	public static void main(String[] args) {
		for(Integer elem : new Quicksort().sort(Arrays.asList(
				new Integer[]{10, 0, 0, -1, -2, 4, 4, 7, 4, 1, 100, -1000}))) {
			System.out.println(elem);
		}
	}
}