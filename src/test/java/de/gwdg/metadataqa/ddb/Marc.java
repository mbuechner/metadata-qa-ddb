package de.gwdg.metadataqa.ddb;

import de.gwdg.metadataqa.api.configuration.ConfigurationReader;
import de.gwdg.metadataqa.api.json.JsonBranch;
import de.gwdg.metadataqa.api.model.EdmFieldInstance;
import de.gwdg.metadataqa.api.schema.Schema;
import de.gwdg.metadataqa.api.xml.OaiPmhXPath;
import org.junit.Before;
import org.junit.Test;
import org.xml.sax.SAXException;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.XPathExpressionException;
import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.List;
import java.util.Map;

import static junit.framework.TestCase.assertEquals;
import static junit.framework.TestCase.assertTrue;

public class Marc {

  String recordAddress = "//marc:record";
  OaiPmhXPath oaiPmhXPath;
  Schema schema;

  @Before
  public void setUpWith() {
    URL url = this.getClass().getResource("/marc/marc.xml");
    File file = new File(url.getFile());
    assertTrue(file.exists());

    try {
      schema = ConfigurationReader.readSchemaYaml("src/main/resources/marc-schema.yaml").asSchema();
      XPathBasedIterator iterator = new XPathBasedIterator(file, recordAddress, schema.getNamespaces());
      String xml = iterator.next();
      Map<String, String> ns = schema.getNamespaces();
      ns.put("xsl", "http://www.w3.org/1999/XSL/Transform");
      oaiPmhXPath = new OaiPmhXPath(xml, ns);
    } catch (XPathExpressionException | IOException | ParserConfigurationException | SAXException e) {
      throw new RuntimeException(e);
    }
  }

  @Test
  public void recordId() {
    JsonBranch p = schema.getPathByLabel("recordId");
    assertEquals("marc:record/marc:controlfield[@tag=\"001\"]", p.getJsonPath());

    List<EdmFieldInstance> itemList = oaiPmhXPath.extractFieldInstanceList(p.getJsonPath());
    assertEquals(1, itemList.size());
    assertEquals("BDR-BV012591623-59024", itemList.get(0).getValue());
  }

  @Test
  public void leader() {
    // JsonBranch p = schema.getPathByLabel("recordId");
    // assertEquals("marc:record/marc:controlfield[@tag=\"001\"]", p.getJsonPath());

    List<EdmFieldInstance> itemList = oaiPmhXPath.extractFieldInstanceList("marc:record/marc:leader");
    assertEquals(1, itemList.size());
    assertEquals("00000nam a2200301 c 4500", itemList.get(0).getValue());
  }

  @Test
  public void subs() {
    // JsonBranch p = schema.getPathByLabel("recordId");
    // assertEquals("marc:record/marc:controlfield[@tag=\"001\"]", p.getJsonPath());

    List<EdmFieldInstance> itemList = oaiPmhXPath.extractFieldInstanceList("substring(marc:record/marc:leader, 7, 1)");
    assertEquals(1, itemList.size());
    assertEquals("a", itemList.get(0).getValue());
  }

}
