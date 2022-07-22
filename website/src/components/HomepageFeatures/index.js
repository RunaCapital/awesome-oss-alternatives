import React from "react";
import styles from "./styles.module.css";
import SearchBarWrapper from "@theme-original/SearchBar";

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container text--center">
        <h2 className="text--center">
          Search for alternatives to your favorite product 👇
        </h2>
        <SearchBarWrapper />
      </div>
    </section>
  );
}
