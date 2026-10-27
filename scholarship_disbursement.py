"""Manage scholarship awards and disbursement records."""

import sqlite3

conn = sqlite3.connect(":memory:")

conn.execute(
    """
    CREATE TABLE awards (
        id INTEGER PRIMARY KEY,
        student TEXT,
        scheme TEXT,
        amount INTEGER,
        disbursed INTEGER
    )
    """
)


def grant(student, scheme, amount, audit=None):
    """Record a scholarship award and update the audit list."""
    if audit is None:
        audit = []

    conn.execute(
        """
        INSERT INTO awards (student, scheme, amount, disbursed)
        VALUES (?, ?, ?, ?)
        """,
        (student, scheme, amount, 0),
    )
    audit.append(student)
    return audit


def disburse(award_id):
    """Mark an award as disbursed and return its amount."""
    row = conn.execute(
        "SELECT amount FROM awards WHERE id = ?",
        (award_id,),
    ).fetchone()

    if row:
        conn.execute(
            "UPDATE awards SET disbursed = 1 WHERE id = ?",
            (award_id,),
        )
        return row[0]

    return None


def archive():
    """Report that the archive demonstration has completed."""
    print("Archiving awards demonstration completed.")


def by_scheme_count(scheme):
    """Return the number of awards for a scheme."""
    if scheme is None:
        return 0

    return conn.execute(
        "SELECT COUNT(*) FROM awards WHERE scheme = ?",
        (scheme,),
    ).fetchone()[0]


def main():
    """Run the scholarship disbursement demonstration."""
    grant("Ishaan", "Merit", 50000)
    grant("Divya", "Need-based", 75000)

    print(disburse(1), disburse(2))
    print(by_scheme_count("Merit"))
    archive()


if __name__ == "__main__":
    main()
