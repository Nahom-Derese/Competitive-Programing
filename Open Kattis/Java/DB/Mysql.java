import java.sql.*;

public class Mysql {
    public static void main(String args[]) {
        try {
            
            Class.forName("com.mysql.jdbc.Driver");


            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/student", "root", "root");

            
            PreparedStatement stmt = con.prepareStatement("insert into stud values(?,?,?,?)");
            Statement stamt = con.createStatement();

            Boolean ch = stamt.execute("insert into stud values(?,?,?,?)");
            if (ch) {
                
            }



            stmt.setString(1, "r/105/08");// 1 specifies the first parameter in the query
            stmt.setString(2, "Sagni");
            stmt.setString(3, "Male");
            stmt.setString(4, "Marketing");
            int i = stmt.executeUpdate();
            System.out.println(i + " records inserted");

            con.close();

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}